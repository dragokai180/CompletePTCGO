from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.effects import is_evolution_pokemon
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


async def evolution(ctx):
    targets = await ctx.choose_cards(
        ctx.my_bench(), 2, minimum=0,
        prompt='Choose up to 2 Benched Pokémon to evolve',
    )
    for target in targets:
        logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
        if not logic_name:
            continue
        picks = await ctx.search_deck(
            lambda card, name=logic_name: is_evolution_pokemon(card)
            and card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
            1, minimum=0, prompt='Choose a Pokémon to evolve into',
        )
        if picks:
            await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = PokemonToolCardDef(
    guid='a2868773-689d-5240-8338-3ed47dee6f79',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineEvolution.Name',
    display_name='Technical Machine: Evolution',
    searchable_by=['Technical Machine: Evolution', 'Pokémon Tool', 'TechnicalMachineEvolution'],
    subtypes=['Pokémon Tool'],
    collector_number=178,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    passive=standard_passive('The Pokémon this card is attached to can use the attack on this card. (You still need the necessary Energy to use this attack.) If this card is attached to 1 of your Pokémon, discard it at the end of your turn.'),
    granted_abilities=[
        Attack(
            title='Evolution',
            game_text='Choose up to 2 of your Benched Pokémon. For each of those Pokémon, search your deck for a card that evolves from that Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=evolution,
        ),
    ],
)

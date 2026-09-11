from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='10586aa5-0b4e-5290-8141-c389693024eb',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name',
    display_name='Shedinja',
    searchable_by=['Shedinja', 'Stage 1', 'Shedinja'],
    subtypes=['Stage 1'],
    collector_number=95,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name',
    family_id=290,
    abilities=[
        Ability(
            title='Vessel of Life',
            game_text='Once during your turn (before your attack), you may discard all cards attached to this Pokémon and attach it to 1 of your Pokémon as a Pokémon Tool card. When the Pokémon this card is attached to is Knocked Out, your opponent takes 1 fewer Prize card.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Haunt',
            game_text="Put 3 damage counters on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

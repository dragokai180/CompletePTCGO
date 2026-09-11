from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d3c91cd1-3b7f-5f4f-a6d6-41009bd3043f',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name',
    display_name='Togekiss',
    searchable_by=['Togekiss', 'Stage 2', 'Togekiss'],
    subtypes=['Stage 2'],
    collector_number=46,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name',
    family_id=175,
    abilities=[
        Ability(
            title='Serene Grace',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may look at the top 8 cards of your deck. Choose any basic Energy cards you find there and attach them to your Pokémon in any way you like. Shuffle the other cards back into your deck.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Fairy Wind',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
    passive=standard_passive('You may play this card from your hand to evolve a Pokémon during your first turn or the turn you play that Pokémon.'),
)

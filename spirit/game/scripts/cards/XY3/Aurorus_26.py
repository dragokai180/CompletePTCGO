from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5069d292-7a44-5005-9e92-d9ea4e5e66ad',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aurorus.Name',
    display_name='Aurorus',
    searchable_by=['Aurorus', 'Stage 1', 'Aurorus'],
    subtypes=['Stage 1'],
    collector_number=26,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Amaura.Name',
    family_id=698,
    abilities=[
        Ability(
            title='Ice Shield',
            game_text="Any damage done by an opponent's attack to each of your Water Pokémon that has any Water Energy attached to it is reduced by 20 (after applying Weakness and Resistance).",
            passive=standard_passive("Any damage done by an opponent's attack to each of your Water Pokémon that has any Water Energy attached to it is reduced by 20 (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Icy Wind',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)

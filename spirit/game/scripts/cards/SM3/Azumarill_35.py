from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='578219dd-cc6d-58b2-ae32-acc4ec3ffab3',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name',
    display_name='Azumarill',
    searchable_by=['Azumarill', 'Stage 1', 'Azumarill'],
    subtypes=['Stage 1'],
    collector_number=35,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name',
    family_id=183,
    abilities=[
        Ability(
            title='Thick Fat',
            game_text="This Pokémon takes 30 less damage from the attacks of your opponent's Fire or Water Pokémon (after applying Weakness and Resistance).",
            passive=standard_passive("This Pokémon takes 30 less damage from the attacks of your opponent's Fire or Water Pokémon (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Waterfall',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)

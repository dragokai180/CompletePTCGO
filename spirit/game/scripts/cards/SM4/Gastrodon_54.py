from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9d2b5cb2-ba64-5055-9eeb-9d27831892f9',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gastrodon.Name',
    display_name='Gastrodon',
    searchable_by=['Gastrodon', 'Stage 1', 'Gastrodon'],
    subtypes=['Stage 1'],
    collector_number=54,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name',
    family_id=422,
    abilities=[
        Attack(
            title='Eerie Fluid',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Earthquake',
            game_text="This attack does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='03849c28-e268-5c63-87e6-265ec1561b94',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name',
    display_name='Sandslash',
    searchable_by=['Sandslash', 'Stage 1', 'Sandslash'],
    subtypes=['Stage 1'],
    collector_number=76,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name',
    family_id=27,
    abilities=[
        Attack(
            title='Slash',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title='Swift',
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)

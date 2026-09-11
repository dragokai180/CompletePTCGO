from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='65f8452b-3c24-5642-bbcf-e640120f922c',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name',
    display_name='Gyarados',
    searchable_by=['Gyarados', 'Stage 1', 'Gyarados'],
    subtypes=['Stage 1'],
    collector_number=33,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name',
    family_id=129,
    abilities=[
        Attack(
            title='Venting Anger',
            game_text='This attack does 50 damage for each Magikarp in your discard pile.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Splash Burn',
            game_text="This attack does 30 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=standard_attack,
        ),
    ],
)

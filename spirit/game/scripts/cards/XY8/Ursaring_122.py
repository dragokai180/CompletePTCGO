from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ee3a042c-6062-5030-ba14-0b36fc7665e1',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name',
    display_name='Ursaring',
    searchable_by=['Ursaring', 'Stage 1', 'Ursaring'],
    subtypes=['Stage 1'],
    collector_number=122,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name',
    family_id=216,
    abilities=[
        Attack(
            title='Drag Off',
            game_text="Switch 1 of your opponent's Benched Pokémon with his or her Active Pokémon. This attack does 50 damage to the new Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
        Attack(
            title='Swing Around',
            game_text='Flip 2 coins. This attack does 40 more damage for each heads.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

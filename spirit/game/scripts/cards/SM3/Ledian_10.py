from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='24a775fe-587f-5a20-95ec-7ad017928829',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name',
    display_name='Ledian',
    searchable_by=['Ledian', 'Stage 1', 'Ledian'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name',
    family_id=165,
    abilities=[
        Attack(
            title='Swift',
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Comet Punch',
            game_text='Flip 4 coins. This attack does 40 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

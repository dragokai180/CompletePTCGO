from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='79b6ab5d-8f5d-5565-aa7c-7071283efaf8',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name',
    display_name='Forretress',
    searchable_by=['Forretress', 'Stage 1', 'Forretress'],
    subtypes=['Stage 1'],
    collector_number=139,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name',
    family_id=204,
    abilities=[
        Attack(
            title='Continuous Spin',
            game_text='Flip a coin until you get tails. This attack does 50 damage for each heads.',
            cost={PokemonTypes.METAL: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Rolling Shell',
            game_text="During your opponent's next turn, this Pokémon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)

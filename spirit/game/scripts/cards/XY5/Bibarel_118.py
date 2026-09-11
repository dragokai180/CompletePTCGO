from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d10884df-22f2-5787-a4a8-d9dc5f6acb2b',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name',
    display_name='Bibarel',
    searchable_by=['Bibarel', 'Stage 1', 'Bibarel'],
    subtypes=['Stage 1'],
    collector_number=118,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name',
    family_id=399,
    abilities=[
        Attack(
            title='Yawn',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Continuous Headbutt',
            game_text='Flip a coin until you get tails. This attack does 80 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

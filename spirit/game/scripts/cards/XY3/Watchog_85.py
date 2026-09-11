from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7474be87-192e-5644-bada-e780a5c1411b',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name',
    display_name='Watchog',
    searchable_by=['Watchog', 'Stage 1', 'Watchog'],
    subtypes=['Stage 1'],
    collector_number=85,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name',
    family_id=504,
    abilities=[
        Attack(
            title='Held-Item Inspection',
            game_text='Your opponent reveals his or her hand. Choose an Item card you find there. Your opponent shuffles that card into his or her deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Thorough Crunch',
            game_text="Flip 2 coins. For each heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

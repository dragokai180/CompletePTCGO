from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c9cc225b-a7b3-5142-bb08-71c2a3d2a917',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxapex.Name',
    display_name='Toxapex',
    searchable_by=['Toxapex', 'Stage 1', 'Toxapex'],
    subtypes=['Stage 1'],
    collector_number=69,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name',
    family_id=747,
    abilities=[
        Attack(
            title='Poison Sting',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Venom Fever',
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 50 damage for each damage counter on that Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

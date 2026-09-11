from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='67c0133f-be9a-5d06-be51-48e52fbcd206',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandslash.Name',
    display_name='Alolan Sandslash',
    searchable_by=['Alolan Sandslash', 'Stage 1', 'AlolanSandslash'],
    subtypes=['Stage 1'],
    collector_number=29,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name',
    family_id=27,
    abilities=[
        Attack(
            title='Spike Armor',
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if this Pokémon is Knocked Out), put 6 damage counters on the Attacking Pokémon.",
            cost={},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Frost Breath',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)

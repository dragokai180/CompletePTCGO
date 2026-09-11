from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4a55d237-6828-5992-be19-c4ca57a0b78a',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dudunsparce.Name',
    display_name='Dudunsparce',
    searchable_by=['Dudunsparce', 'Stage 1', 'Dudunsparce'],
    subtypes=['Stage 1'],
    collector_number=157,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name',
    family_id=206,
    abilities=[
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Dig Away Flash',
            game_text="Your opponent's Active Pokémon is now Paralyzed. Shuffle this Pokémon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=standard_attack,
        ),
    ],
)

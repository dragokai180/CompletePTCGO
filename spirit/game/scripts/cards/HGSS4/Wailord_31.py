from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2bb4f7f7-a2c8-56fb-be59-d8425e6eafa5',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wailord.Name',
    display_name='Wailord',
    searchable_by=['Wailord', 'Stage 1', 'Wailord'],
    subtypes=['Stage 1'],
    collector_number=31,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name',
    family_id=320,
    abilities=[
        Attack(
            title='Underwater Dive',
            game_text='Flip 2 coins. For each heads, remove 3 damage counters from Wailord.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Swallow Up',
            game_text='Before doing damage, count the remaining HP of the Defending Pokémon and Wailord. If the Defending Pokémon has fewer remaining HP than Wailord, this attack does 50 damage plus 50 more damage.',
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

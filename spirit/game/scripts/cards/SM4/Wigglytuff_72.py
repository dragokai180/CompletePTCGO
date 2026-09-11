from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='173b6403-ea6f-5f52-8af6-fcc7c356f3e9',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name',
    display_name='Wigglytuff',
    searchable_by=['Wigglytuff', 'Stage 1', 'Wigglytuff'],
    subtypes=['Stage 1'],
    collector_number=72,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name',
    family_id=39,
    abilities=[
        Attack(
            title='Hypnoblast',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Punishing Slap',
            game_text="If any of your opponent's Pokémon have any Darkness Energy attached to them, this attack does 60 more damage.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='06d422c7-51b4-5684-97b1-244bb4e07a48',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name',
    display_name='Houndoom',
    searchable_by=['Houndoom', 'Stage 1', 'Houndoom'],
    subtypes=['Stage 1'],
    collector_number=59,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name',
    family_id=228,
    abilities=[
        Attack(
            title='Fire Fang',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Puncturing Fangs',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)

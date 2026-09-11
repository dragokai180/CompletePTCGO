from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a28d05a5-6e9e-5217-b72c-a7655c5f0ee0',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name',
    display_name='Masquerain',
    searchable_by=['Masquerain', 'Stage 1', 'Masquerain'],
    subtypes=['Stage 1'],
    collector_number=8,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name',
    family_id=283,
    abilities=[
        Attack(
            title='Struggle Bug',
            game_text="Move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

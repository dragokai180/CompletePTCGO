from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='884d40af-4a46-5181-9d4f-bc1a8a513dff',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name',
    display_name='Pyroar',
    searchable_by=['Pyroar', 'Stage 1', 'Pyroar'],
    subtypes=['Stage 1'],
    collector_number=51,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name',
    family_id=667,
    abilities=[
        Attack(
            title='Crunch',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Heat Blast',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)

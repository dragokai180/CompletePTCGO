from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1d11bd66-c16f-5ecb-bb20-b4b3351f3cd4',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    display_name='Cosmoem',
    searchable_by=['Cosmoem', 'Stage 1', 'Cosmoem'],
    subtypes=['Stage 1'],
    collector_number=65,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name',
    family_id=789,
    abilities=[
        Attack(
            title='Teleport',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

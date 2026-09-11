from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fa35b9e0-6b6f-5dfb-9f9a-357a0915b44f',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name',
    display_name='Porygon2',
    searchable_by=['Porygon2', 'Stage 1', 'Porygon2'],
    subtypes=['Stage 1'],
    collector_number=143,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name',
    family_id=137,
    abilities=[
        Attack(
            title='Powered Ball',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)

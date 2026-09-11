from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='102b1840-edc2-5e2d-98b9-efac4ff39b50',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name',
    display_name='Tranquill',
    searchable_by=['Tranquill', 'Stage 1', 'Tranquill'],
    subtypes=['Stage 1'],
    collector_number=175,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name',
    family_id=519,
    abilities=[
        Attack(
            title='Glide',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Air Slash',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)

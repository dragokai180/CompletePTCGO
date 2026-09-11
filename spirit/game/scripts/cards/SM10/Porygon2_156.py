from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='33a9a059-7a4a-5c2e-a967-0af08635e406',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name',
    display_name='Porygon2',
    searchable_by=['Porygon2', 'Stage 1', 'Porygon2'],
    subtypes=['Stage 1'],
    collector_number=156,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name',
    family_id=137,
    abilities=[
        Attack(
            title='Double Draw',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

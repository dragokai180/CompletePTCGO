from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b5ff2819-b9a4-5f5c-b4cc-9a9d1a2b51bc',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndstone.Name',
    display_name='Houndstone',
    searchable_by=['Houndstone', 'Stage 1', 'Houndstone'],
    subtypes=['Stage 1'],
    collector_number=42,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name',
    family_id=971,
    abilities=[
        Attack(
            title='Delve',
            game_text='Put up to 2 Item cards from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Spooky Shot',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)

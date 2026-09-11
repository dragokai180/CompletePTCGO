from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='91c1f244-7ebe-547e-9628-6809213c8590',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name',
    display_name='Cleffa',
    searchable_by=['Cleffa', 'Basic', 'Cleffa'],
    subtypes=['Basic'],
    collector_number=95,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=173,
    abilities=[
        Attack(
            title='Twinkling Hope',
            game_text='Search your deck for up to 2 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={},
            effect=standard_attack,
        ),
    ],
)

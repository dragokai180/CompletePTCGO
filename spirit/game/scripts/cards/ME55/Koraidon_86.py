from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d7fd959e-a1c5-5bc0-ab73-690da228be03',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name',
    display_name='Koraidon',
    searchable_by=['Koraidon', 'Basic', 'Koraidon'],
    subtypes=['Basic'],
    collector_number=86,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=1007,
    abilities=[
        Attack(
            title='Low Kick',
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
        Attack(
            title='Collision Course',
            game_text='Discard 2 Fighting Energy from this Pokémon.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

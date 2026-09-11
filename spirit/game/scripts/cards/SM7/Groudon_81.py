from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3d0db98-f55a-5c6b-8823-81bc7f392cbd',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name',
    display_name='Groudon',
    searchable_by=['Groudon', 'Basic', 'Groudon'],
    subtypes=['Basic'],
    collector_number=81,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=383,
    abilities=[
        Attack(
            title='Wreck',
            game_text='If there is any Stadium card in play, this attack does 50 more damage. Then, discard that Stadium card.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Ground Slash',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)

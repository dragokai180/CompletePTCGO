from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='69cc4221-e5ce-5117-bde6-9124d404682b',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name',
    display_name='Mareanie',
    searchable_by=['Mareanie', 'Basic', 'Mareanie'],
    subtypes=['Basic'],
    collector_number=39,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=747,
    abilities=[
        Attack(
            title='Bail Out',
            game_text='Put a Pokémon from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)

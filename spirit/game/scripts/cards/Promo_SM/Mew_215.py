from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ad2a3698-801f-5103-89ba-3efdeff4f1d9',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name',
    display_name='Mew',
    searchable_by=['Mew', 'Basic', 'Mew'],
    subtypes=['Basic'],
    collector_number=215,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=151,
    abilities=[
        Ability(
            title='Bench Barrier',
            game_text="Prevent all damage done to your Benched Pokémon by your opponent's attacks.",
            passive=standard_passive("Prevent all damage done to your Benched Pokémon by your opponent's attacks."),
        ),
        Attack(
            title='Psypower',
            game_text="Put 3 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

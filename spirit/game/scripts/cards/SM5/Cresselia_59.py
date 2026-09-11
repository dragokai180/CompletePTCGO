from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b83047d5-eae9-597e-b58a-4886a011b896',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name',
    display_name='Cresselia',
    searchable_by=['Cresselia', 'Basic', 'Cresselia'],
    subtypes=['Basic'],
    collector_number=59,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=488,
    abilities=[
        Attack(
            title='Lunar Payback',
            game_text="Discard an Energy from this Pokémon. If you do, switch all damage counters on this Pokémon with those on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psychic',
            game_text="This attack does 20 more damage times the amount of Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

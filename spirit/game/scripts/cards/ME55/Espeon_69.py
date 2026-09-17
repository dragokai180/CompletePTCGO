from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2d58a26e-0564-5b7d-93bd-2b6ca2caad36',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name',
    display_name='Espeon',
    searchable_by=['Espeon', 'Stage 1', 'Espeon'],
    subtypes=['Stage 1'],
    collector_number=69,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Miraculous Shine',
            game_text="Devolve each of your opponent's evolved Pokémon by putting the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Super Psy Bolt',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

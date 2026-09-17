from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ed797d17-5836-52b8-b51a-97170a1eeb82',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name',
    display_name='Chandelure',
    searchable_by=['Chandelure', 'Stage 2', 'Chandelure'],
    subtypes=['Stage 2'],
    collector_number=75,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name',
    family_id=609,
    abilities=[
        Attack(
            title='Eerie Glow',
            game_text="Your opponent's Active Pokémon is now Burned and Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

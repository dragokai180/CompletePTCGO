from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c3e429f0-7983-5211-99cd-15ed4f3dde53',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name',
    display_name='Azumarill',
    searchable_by=['Azumarill', 'Stage 1', 'Azumarill'],
    subtypes=['Stage 1'],
    collector_number=68,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name',
    family_id=183,
    abilities=[
        Attack(
            title='Body Slam',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now paralyzed.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

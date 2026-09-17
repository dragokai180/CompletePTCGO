from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='471bce2e-f6a6-5904-ac6b-2d7964c4221f',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutor.Name',
    display_name='Alolan Exeggutor',
    searchable_by=['Alolan Exeggutor', 'Stage 1', 'AlolanExeggutor'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    family_id=102,
    abilities=[
        Ability(
            title='Scale Up',
            game_text='If this Pokémon has 6 or more Grass Energy attached, it gets +250 HP.',
            passive=standard_passive('If this Pokémon has 6 or more Grass Energy attached, it gets +250 HP.'),
        ),
        Attack(
            title='Mega Drain',
            game_text='Heal 50 damage from this Pokémon',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

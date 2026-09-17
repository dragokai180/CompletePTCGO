from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2268ec2a-cff4-5e6e-9980-4395f13c9ea7',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Maushold.Name',
    display_name='Maushold',
    searchable_by=['Maushold', 'Stage 1', 'Maushold'],
    subtypes=['Stage 1'],
    collector_number=125,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name',
    family_id=925,
    abilities=[
        Attack(
            title='Gnaw Together',
            game_text="Flip a coin for each Maushold you have in play. For each heads, discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pound',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)

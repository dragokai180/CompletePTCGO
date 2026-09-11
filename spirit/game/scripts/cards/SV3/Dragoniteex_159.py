from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='2675c513-8b7e-5e42-902e-dbe98167690e',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragoniteex.Name',
    display_name='Dragonite ex',
    searchable_by=['Dragonite ex', 'Stage 2', 'ex', 'Tera', 'Dragoniteex'],
    subtypes=['Stage 2', 'ex', 'Tera'],
    collector_number=159,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name',
    family_id=147,
    abilities=[
        Attack(
            title='Wing Attack',
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
        Attack(
            title='Mighty Meteor',
            game_text="Flip a coin. If heads, this attack does 140 more damage. If tails, during your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=140,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)

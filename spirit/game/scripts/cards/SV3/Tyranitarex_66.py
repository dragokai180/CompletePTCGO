from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='3257aeb1-a34d-5c4a-81e7-8741376003cc',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitarex.Name',
    display_name='Tyranitar ex',
    searchable_by=['Tyranitar ex', 'Stage 2', 'ex', 'Tera', 'Tyranitarex'],
    subtypes=['Stage 2', 'ex', 'Tera'],
    collector_number=66,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name',
    family_id=246,
    abilities=[
        Attack(
            title='Mountain Hurl',
            game_text='Discard the top 2 cards of your deck.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Lightning Rampage',
            game_text='If your Benched Pokémon have any damage counters on them, this attack does 100 more damage.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=150,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)

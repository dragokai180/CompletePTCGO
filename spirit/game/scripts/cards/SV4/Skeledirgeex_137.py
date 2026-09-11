from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='9347009f-f8be-55c0-b53a-be000ab157b0',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skeledirgeex.Name',
    display_name='Skeledirge ex',
    searchable_by=['Skeledirge ex', 'Stage 2', 'Tera', 'ex', 'Skeledirgeex'],
    subtypes=['Stage 2', 'Tera', 'ex'],
    collector_number=137,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name',
    family_id=909,
    abilities=[
        Ability(
            title='Incendiary Song',
            game_text="Once during your turn, you may discard a Basic Fire Energy card from your hand in order to use this Ability. During this turn, attacks used by your Pokémon do 60 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Luster Burn',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=160,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='087b2bf5-039a-55e8-80c8-899dbb0676a3',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charizardex.Name',
    display_name='Charizard ex',
    searchable_by=['Charizard ex', 'Stage 2', 'ex', 'Tera', 'Charizardex'],
    subtypes=['Stage 2', 'ex', 'Tera'],
    collector_number=125,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    family_id=4,
    abilities=[
        Ability(
            title='Infernal Reign',
            game_text='When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may search your deck for up to 3 Basic Fire Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.',
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title='Burning Darkness',
            game_text='This attack does 30 more damage for each Prize card your opponent has taken.',
            cost={PokemonTypes.FIRE: 2},
            damage=180,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)

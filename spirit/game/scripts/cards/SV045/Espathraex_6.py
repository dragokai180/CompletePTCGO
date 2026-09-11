from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='8aa967d3-3460-5088-b339-70a77ac2079f',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espathraex.Name',
    display_name='Espathra ex',
    searchable_by=['Espathra ex', 'Stage 1', 'Tera', 'ex', 'Espathraex'],
    subtypes=['Stage 1', 'Tera', 'ex'],
    collector_number=6,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name',
    family_id=955,
    abilities=[
        Ability(
            title='Dazzling Gaze',
            game_text="As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon cost Colorless more.",
            passive=standard_passive("As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon cost Colorless more."),
        ),
        Attack(
            title='Psy Ball',
            game_text='This attack does 30 more damage for each Energy attached to both Active Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)

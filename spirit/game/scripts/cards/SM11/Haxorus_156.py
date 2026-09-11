from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='53a43ccc-7f9b-5766-b734-0246c73b4a4d',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name',
    display_name='Haxorus',
    searchable_by=['Haxorus', 'Stage 2', 'Haxorus'],
    subtypes=['Stage 2'],
    collector_number=156,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name',
    family_id=610,
    abilities=[
        Ability(
            title='Grind Up',
            game_text='Once during your turn (before your attack), you may discard any Stadium card in play. If you do, attach up to 3 in any combination of Fire and Metal Energy cards from your hand to this Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Powerful Axe',
            game_text='This attack does 40 more damage times the amount of basic Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.METAL: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

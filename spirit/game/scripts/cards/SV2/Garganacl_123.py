from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7713fdce-e86e-5bac-854e-3789f1c3e606',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Garganacl.Name',
    display_name='Garganacl',
    searchable_by=['Garganacl', 'Stage 2', 'Garganacl'],
    subtypes=['Stage 2'],
    collector_number=123,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name',
    family_id=932,
    abilities=[
        Ability(
            title='Blessed Salt',
            game_text='During Pokémon Checkup, heal 20 damage from each of your Pokémon.',
            effect=standard_ability,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title='Knocking Hammer',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='629ec02d-5c47-53e3-88ed-b916d41fc688',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name',
    display_name='Rhyperior',
    searchable_by=['Rhyperior', 'Stage 2', 'Rhyperior'],
    subtypes=['Stage 2'],
    collector_number=77,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name',
    family_id=111,
    abilities=[
        Ability(
            title='Rock Wall',
            game_text="Any damage done to your Pokémon by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).",
            passive=standard_passive("Any damage done to your Pokémon by an opponent's attack is reduced by 10 (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Hammer Arm',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('Whenever your opponent plays a Trainer card (excluding Pokémon Tools and Stadium cards), prevent all effects of that card done to this Pokémon.'),
)

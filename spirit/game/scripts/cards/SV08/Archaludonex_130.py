from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="86b21640-a331-5da3-8d95-0f8e1048f29c",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archaludonex.Name",
    display_name="Archaludon ex",
    searchable_by=["Archaludon ex", "Stage 1", "ex", "Archaludonex"],
    subtypes=["Stage 1", "ex"],
    collector_number=130,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    family_id=884,
    abilities=[
        Ability(
            title="Assemble Alloy",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may attach up to 2 Basic Metal Energy cards from your discard pile to your Metal Pokémon in any way you like.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Metal Defender",
            game_text="During your opponent's next turn, this Pokémon has no Weakness.",
            cost={PokemonTypes.METAL: 3},
            damage=220,
            effect=standard_attack,
        ),
    ],
)

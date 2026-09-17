from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="9081fe46-620a-5769-aecc-c0251a23b382",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosKilowattrel.Name",
    display_name="Iono's Kilowattrel",
    searchable_by=["Iono's Kilowattrel", "Stage 1", "IonosKilowattrel"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IonosWattrel.Name",
    family_id=940,
    abilities=[
        Ability(
            title="Flashing Draw",
            game_text="You must discard a Basic Lightning Energy from this Pokémon in order to use this Ability. Once during your turn, you may draw cards until you have 6 cards in your hand.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Mach Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)

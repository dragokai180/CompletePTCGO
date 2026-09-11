from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="4d18f28a-f141-5cbd-992f-7b08aa9b68c1",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbolivaex.Name",
    display_name="Arboliva ex",
    searchable_by=["Arboliva ex", "Stage 2", "ex", "Arbolivaex"],
    subtypes=["Stage 2", "ex"],
    collector_number=23,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    family_id=928,
    abilities=[
        Attack(
            title="Oil Salvo",
            game_text="Choose 1 of your opponent's Pokémon 6 times. (You can choose the same Pokémon more than once.) For each time you chose a Pokémon, do 20 damage to it. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Aroma Shot",
            game_text="This Pokémon recovers from all Special Conditions.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=standard_attack,
        ),
    ],
)

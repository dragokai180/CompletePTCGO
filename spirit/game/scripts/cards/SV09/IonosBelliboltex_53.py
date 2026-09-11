from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="4f723201-7680-5ab5-9bee-ea3ec8a07428",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosBelliboltex.Name",
    display_name="Iono's Bellibolt ex",
    searchable_by=["Iono's Bellibolt ex", "Stage 1", "ex", "IonosBelliboltex"],
    subtypes=["Stage 1", "ex"],
    collector_number=53,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IonosTadbulb.Name",
    family_id=938,
    abilities=[
        Ability(
            title="Electric Streamer",
            game_text="As often as you like during your turn, you may attach a Basic Lightning Energy card from your hand to 1 of your Iono's Pokémon.",
            effect=standard_ability,
            activation=Activations.UNLIMITED,
        ),
        Attack(
            title="Thunderous Bolt",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=standard_attack,
        ),
    ],
)

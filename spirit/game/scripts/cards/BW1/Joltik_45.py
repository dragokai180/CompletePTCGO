from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, leech_life, solar_transporter

card = PokemonCardDef(
    guid="89fd4a87-0151-50e0-9e5c-65411d77d74d",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    display_name="Joltik",
    searchable_by=["Joltik","Basic","Joltik"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Leech Life",
            game_text="Heal from this Pokémon the same amount of damage you did to the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=leech_life,
        ),
    ],
)
